<template>
    <main class="relative min-h-screen overflow-hidden flex flex-col">
        <Navbar activeSection="None" @open-login-popup="toggleLoginPopup" @open-signup-popup="toggleSignupPopup" />
        <img src="@/assets/img/Dots/TitleDots.png" alt="" class="absolute select-none z-0" />

        <div class="flex-grow flex items-center justify-center py-40 overflow-y-auto pb-72">
            
            <PrivacyPolicy v-if="showElement === 'privacy_policy'"  class="z-30"/>
            <TermsOfService v-if="showElement === 'terms_of_service'" class="z-30"/>
            <RulesOfUse v-if="showElement === 'rules_of_use'" class="z-30"/>
        </div>
    
        <LoginPopup v-if="showLoginPopup" @close-popup="toggleLoginPopup" @open-signup="toggleSignupPopup"/>
        <SignupPopup v-if="showSignupPopup" @close-popup="toggleSignupPopup" @open-login="toggleLoginPopup"/>
        <Footer />
    </main>
</template>

<script setup lang="ts">
import PrivacyPolicy from '@/components/Docs/PrivacyPolicy.vue';
import RulesOfUse from '@/components/Docs/RulesOfUse.vue';
import TermsOfService from '@/components/Docs/TermsOfService.vue';
import Navbar from '@/components/Navbar.vue';
import Footer from '@/components/Footer.vue';
import LoginPopup from '@/components/AuthPopups/LoginPopup.vue'
import SignupPopup from '@/components/AuthPopups/RegPopup.vue'

import { computed, ref, watch } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const showElement = computed(() => String(route.params.element));

const showLoginPopup = ref(false);
const showSignupPopup = ref(false);
const toggleLoginPopup = () => {
    showSignupPopup.value = false
    showLoginPopup.value = !showLoginPopup.value
}
const toggleSignupPopup = () => {
    showLoginPopup.value = false
    showSignupPopup.value = !showSignupPopup.value
}

// Watch шо бы наверх скролить когда чел переключается между faq'юшками
watch(route, () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});
</script>
