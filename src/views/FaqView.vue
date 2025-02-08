<template>
    <main class="relative min-h-screen overflow-hidden flex flex-col">
        <Navbar activeSection="faq" @open-login-popup="toggleLoginPopup" @open-signup-popup="toggleSignupPopup" />
        <img src="@/assets/img/Dots/TitleDots.png" alt="" class="absolute select-none z-0" />

        <div class="flex-grow flex items-center justify-center py-40 overflow-y-auto pb-72">
            <Faq class="z-30"/>
        </div>
    
        <LoginPopup v-if="showLoginPopup" @close-popup="toggleLoginPopup" @open-signup="toggleSignupPopup"/>
        <SignupPopup v-if="showSignupPopup" @close-popup="toggleSignupPopup" @open-login="toggleLoginPopup"/>
        <Footer />
    </main>
</template>

<script setup lang="ts">
import Faq from '@/components/Faq/Faq.vue';
import Navbar from '@/components/Navbar.vue';
import Footer from '@/components/Footer.vue';
import LoginPopup from '@/components/AuthPopups/LoginPopup.vue'
import SignupPopup from '@/components/AuthPopups/RegPopup.vue'

import { computed, ref, watch } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();

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

</script>
