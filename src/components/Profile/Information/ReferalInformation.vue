<template>
    <div class="flex-grow space-y-5">
        <div class="bg-custom-black-adventage border-bottom-custom-adventage rounded-xl flex flex-col md:flex-row p-5">

            <div class="w-full h-full space-y-2"> 
                <div class="flex flex-wrap justify-between">
                    <div class="flex flex-row text-xl gap-x-2 items-center">
                        <img src="@/assets/img/icons/Profile/Info/Refferal.svg" class="w-6 h-6">
                        <span class="text-white">Your Refferal Code</span>
                    </div>

                    <div class="text-xl">
                        <span class="custom-gradient-text-title-main">{{ user?.refferal_system?.code }}</span>
                    </div>
                </div>

                <div class="flex flex-wrap justify-between gap-y-2">
                    <div class="flex flex-row text-xl gap-x-2 items-center">
                        <img src="@/assets/img/icons/Profile/Info/RefferalNum.svg" class="w-6 h-6">
                        <span class="text-white">Number Of Refferals</span>
                    </div>

                    <div class="text-xl">
                        <span class="custom-gradient-text-title-main">{{ user?.refferal_system?.refferal_number }}</span>
                    </div>
                </div>

                <div class="flex flex-wrap justify-between gap-y-2">
                    <div class="flex flex-row text-xl gap-x-2 items-center">
                        <img src="@/assets/img/icons/Profile/Info/RefferalBonus.svg" class="w-6 h-6">
                        <span class="text-white">Refferal Bonus Earned</span>
                    </div>

                    <div class="text-xl">
                        <span class="custom-gradient-text-title-main">{{ user?.refferal_system?.refferal_bonus }}</span>
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
  
