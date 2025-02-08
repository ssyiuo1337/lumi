<template>
    <button
        @click="handleClick">
        <img
            src="@/assets/img/Profile/Change.svg">
        </img>
    </button>
    
    <!-- Модальное окно -->
    <div
        v-if="showModal"
        class="fixed left-0 top-0 z-50 w-full h-full flex items-center justify-center bg-black bg-opacity-50"
        @click.self="showModal=false">
        <div
            class="bg-custom-black-adventage rounded-xl shadow-lg w-full md:max-w-md mx-auto p-8 relative z-60"
            @click.stop>
            <div class="flex flex-col gap-y-3">
                
                <div>
                    <div class="flex flex-row items-center justify-between">
                    <label for="referral" class="block text-white mb-1">Old Password</label>
                    </div>
                    <div class="relative mb-4">
                    <input 
                        id="referral"
                        v-model="old_password" 
                        placeholder="Old Password" 
                        type="password" 
                        class="w-full border-gray-300 rounded-md px-10 py-2 bg-custom-back-popup-input custom-border-popup text-white"
                    >
                    <img 
                        src="@/assets/img/icons/Auth/lock.png" 
                        alt="Referral Icon" 
                        class="absolute left-3 top-1/2 transform -translate-y-1/2 w-5 h-5">
                    </div>
                </div>

                <div>
                    <div class="flex flex-row items-center justify-between">
                    <label for="referral" class="block text-white mb-1">New Password</label>
                    </div>
                    <div class="relative mb-4">
                    <input 
                        id="referral"
                        v-model="new_password" 
                        placeholder="New Password" 
                        type="password" 
                        class="w-full border-gray-300 rounded-md px-10 py-2 bg-custom-back-popup-input custom-border-popup text-white"
                    >
                    <img 
                        src="@/assets/img/icons/Auth/lock.png" 
                        alt="Referral Icon" 
                        class="absolute left-3 top-1/2 transform -translate-y-1/2 w-5 h-5">
                    </div>
                </div>
        
                <button 
                    class="flex items-center justify-center text-white bg-custom-gradient rounded-md px-4 py-1.5 text-lg shadow-custom w-full"
                    @click="changePassword">
                    Change
                </button>
            </div>
        </div>
    </div>
    
    <notifications group="error" position="bottom left" class="z-50"/>
</template>
  
<script setup>
    import { computed, ref } from 'vue';;
    import httpClient from '@/services/ApiService';

    import { notify } from "@kyvg/vue3-notification";

    const showModal = ref(false);
  
    const old_password = ref('')
    const new_password = ref('')
    const message = ref('');

    const handleClick = () => {
        showModal.value = true;
    };

    const changePassword = async () => {
        try {
            const response = await httpClient.patch('auth/change_password/', {
                old_password: old_password.value,
                new_password: new_password.value,
            });

            sessionStorage.setItem('passwordChanged', 'true');
            window.location.reload();
        } catch (error) {
            message.value = error.response?.data?.error || 'Произошла ошибка при смене пароля';
            notify({
                group: "error",
                type: "error",
                title: "Change Password",
                text: message.value,
            });
        }
    };
  
</script>
  
  