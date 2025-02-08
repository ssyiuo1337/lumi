<template>
    <div class="flex flex-col gap-y-3 grow-0 md:px-0 p-4 w-full lg:w-fit">
        <div class="relative border-bottom-custom-adventage flex flex-col md:flex-row items-center bg-custom-black-adventage p-6 gap-y-3 md:gap-x-5 rounded-xl">
            
            <img src="@/assets/img/Profile/glow.svg" class="absolute z-10 w-full h-full pointer-events-none" >
            
            <img src="@/assets/img/ReviewsAvatars/test.jpeg" class="w-24 h-24 rounded-full ring-2 ring-[#D4CDFF] ring-offset-4 ring-offset-[#09090D]">


            <div class="relative flex flex-col text-center md:text-left z-10 lg:max-w-xl break-all">
                <div class="flex flex-col md:flex-row gap-y-1 md:gap-x-1 text-3xl">
                    <h1 class="text-white">{{ user?.username }}</h1>
                    <h1 class="custom-gradient-text-title-main">[ {{ user?.role }} ]</h1>
                </div>
                <h1 class="text-[#4F4F53] p-1.5 bg-[#131317] w-fit h-fit rounded-md text-xl text-center">UID: {{ user?.id }}</h1>
            </div>
        </div>

        <div class="w-full flex flex-col gap-y-2" v-if="user?.private">
            <div class="w-full flex flex-col md:flex-row justify-between gap-y-2 md:gap-x-2">
                <button 
                    class="border-bottom-custom-adventage flex flex-row items-center justify-center bg-custom-black-adventage rounded-xl py-2 px-4 md:px-10 grow gap-x-1 text-white text-xl"
                    @click="download">
                    <img src="@/assets/img/icons/Profile/download.svg">
                    Download
                </button>

                <button 
                    class="border-bottom-custom-adventage flex flex-row items-center justify-center bg-custom-black-adventage rounded-xl py-2 px-4 md:px-10 grow gap-x-1 text-white text-xl"
                    @click="beta">
                    <img src="@/assets/img/icons/Profile/beta.svg">
                    Buy Beta
                </button>
            </div>

            <div class="w-full flex flex-col gap-y-2">
                <KeyPopup />

                <button 
                    class="border-bottom-custom-adventage flex flex-row items-center justify-center bg-custom-black-adventage rounded-xl py-2 px-4 md:px-10 grow gap-x-1 text-white text-xl"
                    @click="signOut">
                    <img src="@/assets/img/icons/Profile/SignOut.svg">
                    Sign Out
                </button>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { useUserStore } from '@/stores/UserStore'
import { useRouter } from 'vue-router';
import { computed, onMounted } from 'vue';

import { notify } from "@kyvg/vue3-notification";
import AuthService from '@/services/AuthService';
import KeyPopup from './KeyPopup.vue';

const userStore = useUserStore();
const router = useRouter();

const user = computed(() => userStore.user);

const download = () => {
    notify({
            group: "nahui",
            type: "error",
            title: "Download error",
            text: "Not available now :(",
        });
}
const beta = () => {
    notify({
            group: "nahui",
            type: "error",
            title: "Buying Beta error",
            text: "Not available now :(",
        });
}

const signOut = async () => {
    try {
        AuthService.logout(); 
        await router.push({ name: 'main' });
    } catch (error) {
        console.error('Error during sign out:', error);
    }
};

</script>
