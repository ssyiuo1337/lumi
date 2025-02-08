<template>
    <button 
        class="border-bottom-custom-adventage flex flex-row items-center justify-center bg-custom-black-adventage rounded-xl py-2 px-4 md:px-10 grow gap-x-1 text-white text-xl"
        @click="handleClick">
        <img src="@/assets/img/icons/Profile/ActivateKey.svg">
        Activate Key
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
                    <label for="sub_key" class="block text-white mb-1">Key</label>
                    </div>
                    <div class="relative mb-4">
                    <input 
                        id="sub_key"
                        v-model="key" 
                        placeholder="Subscription Key" 
                        type="text" 
                        class="w-full border-gray-300 rounded-md px-10 py-2 bg-custom-back-popup-input custom-border-popup text-white"
                    >
                    <img 
                        src="@/assets/img/icons/Profile/ActivateKey.svg"
                        alt="Key Icon" 
                        class="absolute left-3 top-1/2 transform -translate-y-1/2 w-5 h-5">
                    </div>
                </div>
        
                <button 
                    class="flex items-center justify-center text-white bg-custom-gradient rounded-md px-4 py-1.5 text-lg shadow-custom w-full"
                    @click="activateKey">
                    Activate
                </button>
            </div>
        </div>
    </div>
    
    <notifications group="keyError" position="bottom left" class="z-50"/>
</template>
  
<script setup>
    import { computed, ref } from 'vue';;
    import httpClient from '@/services/ApiService';

    import { notify } from "@kyvg/vue3-notification";

    const showModal = ref(false);
  
    const key = ref('')

    const handleClick = () => {
        showModal.value = true;
    };


    const activateKey = async () => {
        console.log("activate")
        try {

            await httpClient.post('sub/activate_key/', {
                key: key.value,
            });
            sessionStorage.setItem('keyActivated', 'true');
            window.location.reload();
        } catch (error) {
            notify({
                group: "keyError",
                type: "error",
                title: "Key activation error",
                text: "Invalid or expired key",
            });
        }
    }
  
</script>
  
  