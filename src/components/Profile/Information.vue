<template>
  <div class="relative flex-grow space-y-5 p-4">
    <MainInformation />
    <LaunchInformation v-if="user?.role !== 'VISITOR'"/>

    <ReferalInformation v-if="hasReferralSystem && user?.refferal_system?.refferal_available"/>
    <ReferalUnvailable v-else/>

    <img class="absolute top-0 right-0 h-full z-10 mask-image pointer-events-none" src="@/assets/img/Profile/InformationGlow.svg">

  </div>
</template>

<script setup lang="ts">
import MainInformation from '@/components/Profile/Information/MainInformation.vue'
import LaunchInformation from '@/components/Profile/Information/LaunchInformation.vue'
import ReferalInformation from '@/components/Profile/Information/ReferalInformation.vue'
import ReferalUnvailable from '@/components/Profile/Information/ReferalUnvailable.vue'
import { useUserStore } from '@/stores/UserStore'

import { computed } from 'vue';

const userStore = useUserStore();
const user = computed(() => userStore.user);

const hasReferralSystem = computed(() => {
    return userStore.user !== null && userStore.user.refferal_system !== undefined;
});

</script>

<style scoped>
    .mask-image {
        -webkit-mask-image: linear-gradient(to right, transparent, black 50%, transparent);
        mask-image: linear-gradient(to right, transparent, black 50%, transparent);
  }
</style>
