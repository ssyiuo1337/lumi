import httpClient from './ApiService';
import axios, { AxiosError } from 'axios';

const API_BASE_URL = 'https://lumi-24al.onrender.com/api/v1'; // ЭТО СУКА ВАЖНО // ЧТОБЫ НЕ ЗАБЫТЬ
const MAX_RETRIES = 3;
const RETRY_DELAY = 1000; // 1 second

class AuthService {
  setUsername(username: string): void {
    localStorage.setItem('username', username);
  }
  getUsername(): string | null {
    return localStorage.getItem('username');
  }

  setJwtToken(token: string): void {
    localStorage.setItem('jwtToken', token);
  }
  setRefreshToken(token: string): void {
    localStorage.setItem('refreshToken', token);
  }

  getJwtToken(): string | null {
    return localStorage.getItem('jwtToken');
  }
  getRefreshToken(): string | null {
    return localStorage.getItem('refreshToken');
  }

  clearTokens(): void {
    localStorage.removeItem('jwtToken');
    localStorage.removeItem('refreshToken');
    localStorage.removeItem('username');
  }

  isAuthenticated(): boolean {
    const jwtToken = this.getJwtToken();
    return jwtToken !== null;
  }

  async register(username: string, password: string, email: string, token: string): Promise<void> {
    try {
      const response = await httpClient.post('http://127.0.0.1:8000/api/v1/auth/register/', {
        username,
        password,
        email,
        token,
      });
      const { access, refresh } = response.data;
      this.setUsername(username);


      this.setJwtToken(access);
      this.setRefreshToken(refresh);
    } catch (error) {
      console.error('Registration failed:', error);
      throw error;
    }
  }

  private async retryRequest<T>(fn: () => Promise<T>, retries = MAX_RETRIES): Promise<T> {
    try {
      return await fn();
    } catch (error) {
      if (retries > 0 && axios.isAxiosError(error) && !error.response) {
        // Only retry on network errors (no response)
        await new Promise(resolve => setTimeout(resolve, RETRY_DELAY));
        return this.retryRequest(fn, retries - 1);
      }
      throw error;
    }
  }

  async login(login: string, password: string): Promise<string> {
    try {
      const response = await this.retryRequest(() =>
        httpClient.post(`${API_BASE_URL}/auth/login/`, {
          login,
          password,
        })
      );

      const { access, refresh, username } = response.data;
      this.setJwtToken(access);
      this.setRefreshToken(refresh);
      this.setUsername(username);
      return username;

    } catch (error) {
      if (axios.isAxiosError(error)) {
        if (!error.response) {
          throw {
            status: 0,
            data: {
              detail: 'Network error: Unable to connect to the server'
            }
          };
        }
        throw {
          status: error.response.status,
          data: error.response.data,
        };
      }
      console.error('Unexpected error occurred:', error);
      throw {
        status: 500,
        data: {
          detail: 'An unexpected error occurred'
        }
      };
    }
  }

  logout(): void {
    this.clearTokens();
  }
}

export default new AuthService();
