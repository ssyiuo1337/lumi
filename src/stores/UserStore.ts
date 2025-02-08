import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import type { User } from '@/types/user'
import httpClient from '@/services/ApiService'
import AuthService from '@/services/AuthService'

export const useUserStore = defineStore('userStore', () => {

    const user = ref<User | null>(null);

    // Получение публичной информации о пользователе по username
    const fetchUser = async (username: string) => {
        try {
            const response = await httpClient.get(`stat/get_user/${username}/`);
            user.value = response.data;
            if (user.value) {
                user.value.private = false;
            }
        } catch (error) {
            console.error('Error fetching public user data:', error);
        }
    }

    // Получение приватной информации о текущем аутентифицированном пользователе
    const fetchPrivateUserInfo = async () => {
        try {
            if (!AuthService.isAuthenticated()) {
                throw new Error('User is not authenticated');
            }

            const response = await httpClient.get('stat/get_myself/');
            user.value = response.data;

            if (user.value) {
                user.value.private = true;
            }

        } catch (error) {
            console.error('Error fetching private user data:', error);
        }
    }

    return {
        user,
        fetchUser,
        fetchPrivateUserInfo
    }
})
