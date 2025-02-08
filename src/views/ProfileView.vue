<template>
    <main class="relative min-h-screen overflow-hidden pb-40" ref="main">
        <Navbar :activeSection="null" @open-login-popup="toggleLoginPopup" @open-signup-popup="toggleSignupPopup" />
      
        <div class="flex flex-wrap w-full h-full px-8 lg:px-40 mt-[95px] gap-x-2 pb-36 justify-center ">

            <Avatar />
            <Information />

            <notifications group="success"  position="bottom left" class="z-50"/>
            <notifications group="nahui"  position="bottom left" class="z-50"/>

        </div>

        <LoginPopup v-if="showLoginPopup" @close-popup="toggleLoginPopup" @open-signup="toggleSignupPopup"/>
        <SignupPopup v-if="showSignupPopup" @close-popup="toggleSignupPopup" @open-login="toggleLoginPopup"/>
        <Footer />
    </main>
</template>

<script setup lang="ts">
import { onMounted, ref, computed } from 'vue';
import { useRoute } from 'vue-router';
import { notify } from "@kyvg/vue3-notification";

import Navbar from '../components/Navbar.vue';
import Footer from '@/components/Footer.vue';
import Avatar from '@/components/Profile/Avatar.vue';
import Information from '@/components/Profile/Information.vue';
import { useUserStore } from '@/stores/UserStore'
import AuthService from '@/services/AuthService';

import LoginPopup from '@/components/AuthPopups/LoginPopup.vue'
import SignupPopup from '@/components/AuthPopups/RegPopup.vue'

const route = useRoute()
const userStore = useUserStore()

const showLoginPopup = ref(false)
const showSignupPopup = ref(false)

const toggleLoginPopup = () => {
    showSignupPopup.value = false
    showLoginPopup.value = !showLoginPopup.value
}
const toggleSignupPopup = () => {
    showLoginPopup.value = false
    showSignupPopup.value = !showSignupPopup.value
}

onMounted(() => {
    const username = route.params.username as string
    const currentUser = AuthService.getUsername();

    if (username === currentUser) {
        userStore.fetchPrivateUserInfo();
    } else {
        userStore.fetchUser(username);
    }

    if (sessionStorage.getItem('passwordChanged') === 'true') {
        notify({
            group: "success",
            type: "success",
            title: "Change Password",
            text: "Password changed successfully",
        });
        sessionStorage.removeItem('passwordChanged');
    }

    if (sessionStorage.getItem('keyActivated') === 'true') {
        notify({
            group: "success",
            type: "success",
            title: "Key activation",
            text: "Key activated successfully",
        });
        sessionStorage.removeItem('keyActivated');
    }
})

</script>
