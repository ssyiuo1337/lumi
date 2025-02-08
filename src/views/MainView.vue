<template>
    <main class="relative min-h-screen select-none overflow-hidden" @scroll="handleScroll" ref="main">
        <Navbar :activeSection="activeSection" @open-login-popup="toggleLoginPopup" @open-signup-popup="toggleSignupPopup" />
        
        <div id="sectionAbout" class="flex items-center justify-center w-full h-screen lg:px-40">
            <Title />
        </div>

        <div id="sectionAbout" class="flex items-center justify-center w-full h-fit p-4 overfloiw-hidden lg:px-40">
            <Adventages />
        </div>

        <div id="sectionReviews" class="flex items-center justify-center w-full h-screen lg:px-40 ">
            <Reviews />
        </div>

        <div id="sectionPricing" class="flex items-center justify-center w-full h-screen mb-72 lg:px-40">
            <Pricing />
        </div>

        <LoginPopup v-if="showLoginPopup" @close-popup="toggleLoginPopup" @open-signup="toggleSignupPopup"/>
        <SignupPopup v-if="showSignupPopup" @close-popup="toggleSignupPopup" @open-login="toggleLoginPopup"/>
        <Footer />
    </main>
</template>

<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount } from 'vue'

import Navbar from '../components/Navbar.vue'
import Title from '../components/Title.vue'
import Adventages from '@/components/Adventages.vue'

import Reviews from '@/components/Reviews/Reviews.vue'
import Pricing from '@/components/Buy/Pricing.vue'
import Footer from '@/components/Footer.vue'

import LoginPopup from '@/components/AuthPopups/LoginPopup.vue'
import SignupPopup from '@/components/AuthPopups/RegPopup.vue'

const showLoginPopup = ref(false)
const showSignupPopup = ref(false)

const activeSection = ref('about')

const sections = ref<Record<string, HTMLDivElement | null>>({
    about: null,
    reviews: null,
    pricing: null,
})

const handleScroll = () => {
    const scrollPosition = window.scrollY + window.innerHeight / 2
    for (const [key, element] of Object.entries(sections.value)) {
        if (element && scrollPosition >= element.offsetTop && scrollPosition < element.offsetTop + element.offsetHeight) {
            activeSection.value = key
        break
        }
    }
}

const toggleLoginPopup = () => {
    showSignupPopup.value = false
    showLoginPopup.value = !showLoginPopup.value
}
const toggleSignupPopup = () => {
    showLoginPopup.value = false
    showSignupPopup.value = !showSignupPopup.value
}

onMounted(() => {
    sections.value.about = document.getElementById('sectionAbout') as HTMLDivElement
    // sections.value.adventages = document.getElementById('sectionAdventages') as HTMLDivElement
    sections.value.reviews = document.getElementById('sectionReviews') as HTMLDivElement
    sections.value.pricing = document.getElementById('sectionPricing') as HTMLDivElement
    window.addEventListener('scroll', handleScroll)
})

onBeforeUnmount(() => {
    window.removeEventListener('scroll', handleScroll)
})
</script>
