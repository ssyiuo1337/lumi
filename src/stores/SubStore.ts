// stores/subscriptionStore.js
import { defineStore } from 'pinia';
import { ref } from 'vue';

type Plan = {
    sub_type: string;
    ref_code?: string;
};

export const useSubscriptionStore = defineStore('subscription', () => {

    const selectedPlan = ref<Plan | null>(null);

    const setSubType = (subType: string) => {
        if (selectedPlan.value) {
            selectedPlan.value.sub_type = subType;
        } else {
            selectedPlan.value = { sub_type: subType };
        }
    };

    const setRefCode = (refCode: string) => {
        if (selectedPlan.value) {
            selectedPlan.value.ref_code = refCode;
        } else {
            selectedPlan.value = { sub_type: '', ref_code: refCode };
        }
    };

    return {
        selectedPlan,
        setSubType,
        setRefCode,
    };
});
