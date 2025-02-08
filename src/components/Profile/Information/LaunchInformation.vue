<template>
    <div class="flex-grow space-y-5">
        <div class="bg-custom-black-adventage border-bottom-custom-adventage rounded-xl flex flex-col md:flex-row p-5 w-full">

            <div class="w-full h-full space-y-2"> 
                <div class="flex flex-wrap justify-between">
                    <div class="flex flex-row text-xl gap-x-2 items-center">
                        <img src="@/assets/img/icons/Profile/Info/NumOfLaunch.svg" class="w-6 h-6">
                        <span class="text-white">Number of Launches</span>
                    </div>

                    <div class="text-xl">
                        <span class="custom-gradient-text-title-main">{{ user?.statistics?.launch_number }}</span>
                    </div>
                </div>

                <div class="flex flex-wrap justify-between gap-y-2">
                    <div class="flex flex-row text-xl gap-x-2 items-center">
                        <img src="@/assets/img/icons/Profile/Info/PlayTime.svg" class="w-6 h-6">
                        <span class="text-white">Playtime</span>
                    </div>

                    <div class="text-xl">
                        <span class="custom-gradient-text-title-main">{{ user?.statistics?.playtime }}</span>
                    </div>
                </div>
            </div>
            
        </div>
    </div>
</template>
  
<script setup lang="ts">
import { useUserStore } from '@/stores/UserStore'

import { computed } from 'vue';

const userStore = useUserStore();
const user = computed(() => userStore.user);
</script>
  
