<template>
    <!-- Modal -->
    <div
      class="fixed left-0 top-0 z-50 w-full h-full flex items-center justify-center bg-black bg-opacity-50"
      @click.self="closePopup"
    >
      <div
        class="bg-custom-black-adventage rounded-xl shadow-lg w-full md:max-w-md mx-auto p-8 z-50 overflow-y-auto"
        @click.stop
      >
        <!-- Modal body -->
        <div class="flex flex-col gap-y-3">
            <div>
              <label for="login" class="block text-white mb-1">Username or email</label>
              <div class="relative mb-4">
                <input
                  id="login"
                  v-model="login"
                  placeholder="Username or email"
                  type="email"
                  class="w-full border-gray-300 rounded-md px-10 py-2 bg-custom-back-popup-input custom-border-popup text-white"
                >
                <img
                  src="@/assets/img/icons/Auth/user.png"
                  alt="User Icon"
                  class="absolute left-3 top-1/2 transform -translate-y-1/2 w-5 h-5"
                >
              </div>
            </div>

            <div>
              <div class="flex flex-row items-center justify-between">
                <label for="password" class="block text-white mb-1">Password</label>
                <!-- <a href="" class="custom-gradient-text-title">Forgot Password?</a> -->
              </div>
              <div class="relative">
                <input
                  id="password"
                  type="password"
                  v-model="password"
                  placeholder="Password"
                  class="w-full border-gray-300 rounded-md pl-10 py-2 bg-custom-back-popup-input custom-border-popup text-white"
                >
                <img
                  src="@/assets/img/icons/Auth/lock.png"
                  alt="Lock Icon"
                  class="absolute left-3 top-1/2 transform -translate-y-1/2 w-5 h-5"
                >
              </div>
            </div>

            <div class="flex items-center mb-4">
              <input id="checkbox" type="checkbox" value="" class="w-4 h-4 bg-main accent-main">
              <label for="checkbox" class="ms-2 text-white">Remember Me</label>
            </div>

            <button
              class="flex items-center justify-center text-white bg-custom-gradient rounded-md px-4 py-1.5 text-lg shadow-custom w-full"
              @click="handleLogin">
            <svg
              class="animate-spin block -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
              :class="{'hidden': !loading}">
              <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
              <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
              Log in
            </button>

            <div class="flex flex-row gap-x-2 flex items-center justify-center">
                <span class="text-white">Do not have an account?</span>
                <a href="" class="text-main" @click.prevent="openSignup">Signup</a>
            </div>
          </div>

        </div>
    </div>
    <notifications group="auth_error" position="bottom left" class="z-50"/>
  </template>

  <script setup lang="ts">
      import { ref, defineEmits, onMounted } from 'vue'
      import { useRouter } from 'vue-router';
      import { notify } from "@kyvg/vue3-notification";

      import AuthService from '@/services/AuthService';
      import { useUserStore } from '@/stores/UserStore'

      const store = useUserStore()

      const emit = defineEmits(['close-popup', 'open-signup'])
      const router = useRouter();

      const login = ref<string>('')
      const password = ref<string>('')
      const loading = ref(false)

      const closePopup = () => {
          emit('close-popup')
      }

      const openSignup = () => {
          emit('open-signup')
      }

      const handleLogin = async () => {
          if (!login.value || !password.value) {
              notify({
                  group: "auth_error",
                  type: "error",
                  title: "Empty fields",
                  text: "Please enter Login and Password.",
              });
              return;
          }
          try {
              loading.value = true
              const username = await AuthService.login(login.value, password.value);
              console.log('Logged in user:', username);
              await store.fetchPrivateUserInfo();
              closePopup()
              router.push({ name: 'profile', params: { username: String(username) } });
          } catch (error) {
              loading.value = false
              if (typeof error === 'object' && error !== null && 'status' in error && 'data' in error) {
                  const err = error as { status: number; data: any };

                  const errorMessages: Record<number, string> = {
                      400: 'Please check your input and try again',
                      401: 'Invalid username/email or password',
                      403: 'Your account is not authorized',
                      404: 'Login service is currently unavailable',
                      405: 'Invalid request method',
                      500: 'Server error, please try again later'
                  };

                  const errorMessage = err.data?.detail || errorMessages[err.status] || "Login failed";

                  notify({
                      group: "auth_error",
                      type: "error",
                      title: "Login Error",
                      text: errorMessage
                  });

                  if (err.status === 401) {
                      password.value = ''; // Clear password on invalid credentials
                  }
              } else {
                  notify({
                      group: "auth_error",
                      type: "error",
                      title: "Connection Error",
                      text: "Unable to connect to the server. Please check your internet connection."
                  });
              }
          } finally {
              loading.value = false;
          }
      };

  onMounted(() => {
      loading.value = false
  });

  </script>
