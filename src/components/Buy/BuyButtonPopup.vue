<template>
  <button
    :disabled="!isPlanSelected"
    :class="[
      'flex items-center rounded-md px-4 py-2 text-3xl transition-shadow duration-200 text-white',
      isPlanSelected
        ? 'shadow-[0_4px_15px_rgba(255,255,255,0.5)] cursor-pointer bg-custom-gradient'
        : 'shadow-none cursor-not-allowed opacity-80 bg-custom-gradient'
    ]"
    @click="handleClick">
    {{ $t('pricing.button') }}
    <img src="@/assets/img/icons/buyico.svg" alt="icon" class="ml-2 w-10 h-10">
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
            <label for="referral" class="block text-white mb-1">Refferal code</label>
            <a
                class="text-[#A39BD6]"
                @click="getPayment()">
                No code? Do nothing
            </a>
          </div>
          <div class="relative mb-4">
            <input 
              id="referral"
              v-model="ref_code" 
              placeholder="Refferal code" 
              type="text" 
              class="w-full border-gray-300 rounded-md px-10 py-2 bg-custom-back-popup-input custom-border-popup text-white"
            >
            <img 
              src="@/assets/img/icons/Pricing/RefferalIcon.svg" 
              alt="Referral Icon" 
              class="absolute left-3 top-1/2 transform -translate-y-1/2 w-5 h-5">
          </div>
        </div>

        <button 
          class="flex items-center justify-center text-white bg-custom-gradient rounded-md px-4 py-1.5 text-lg shadow-custom w-full"
          @click="setReferralCode(ref_code)">
          Activate
        </button>
      </div>
    </div>
  </div>

  <notifications group="refferal" position="bottom left" class="z-50"/>

</template>

<script setup>
import { computed, ref } from 'vue';
import { notify } from "@kyvg/vue3-notification";

import { useSubscriptionStore } from '@/stores/SubStore';
import httpClient from '@/services/ApiService';

const subscriptionStore = useSubscriptionStore();
const isPlanSelected = computed(() => !!subscriptionStore.selectedPlan);
const showModal = ref(false);

const ref_code = ref('')

const handleClick = () => {
    if (isPlanSelected.value) {
        showModal.value = true;
    }
};

const checkReferralCode = async (code) => {
    try {
        await httpClient.get('stat/check_ref/', {
            params: { code: code }
        });
        return true; 
    } catch (error) {
        console.error('Error checking referral code:', error);
        return false;
    }
};

const setReferralCode = async (code) => {
    const isValid = await checkReferralCode(code);
    
    if (isValid) {
        subscriptionStore.setRefCode(code);
        console.log(subscriptionStore);
        notify({
            group: "refferal",
            type: "success",
            title: "Success",
            text: "Refferal code activated",
        });
        getPayment();
    } else {
        console.log("error");
        notify({
            group: "refferal",
            type: "error",
            title: "Error",
            text: "No such refferal code!",
        });
    }
    
    getPayment();
};

const getPayment = () => {
    const sub_info = subscriptionStore.selectedPlan
    console.log("ПЕЙМЕНТ!")
}
</script>

