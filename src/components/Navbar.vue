<template>
    <div class="fixed w-full z-40 bg-navbar-bg border-bottom-custom bg-opacity-25 backdrop-blur-md lg:px-40 px-5">
      <img src="@/assets/img/NavbarGlow.svg" class="absolute z-0 pointer-events-none">
      <nav class="relative max-w-screen-xl mx-auto flex items-center shadow-dark-mild z-50 nav-border py-2 h-[76px]">
        <!-- Логотип -->
        <div class="flex-1 flex items-center gap-x-10 ">
            <router-link :to="{ name: 'main' }">
                <img class="h-10 w-10 md:h-10 md:w-10 lg:h-10 lg:w-10 hover:animate-pulse" src="../assets/img/Avatar.svg" alt="TE Logo" loading="lazy" />
            </router-link>
            <div class="flex justify-end gap-2.5 z-50">
                <button
                    @click="switchLanguage('en-US')"
                    :class="{'bg-gray-800 text-white': currentLanguage !== 'en-US', 'bg-green-600 text-white': currentLanguage === 'en-US'}"
                    class="px-4 py-2 rounded-lg transition-colors duration-300">
                    EN
                </button>
                <button
                    @click="switchLanguage('ru-RU')"
                    :class="{'bg-gray-800 text-white': currentLanguage !== 'ru-RU', 'bg-green-600 text-white': currentLanguage === 'ru-RU'}"
                    class="px-4 py-2 rounded-lg transition-colors duration-300">
                    RU
                </button>
            </div>
        </div>
  
        <!-- Меню страниц -->
        <RouterLink class="hidden lg:flex flex-1 justify-center w-full" :to="{ name: 'main' }">
          <div class="flex gap-2.5 text-xl">
            <a 
              href="#sectionAbout" 
              class="menu-item flex-1" 
              :class="{ 'active': activeSection === 'about' }"
              @click="scrollToSection('about')">
              {{ $t('navbar.about') }}
              <span v-if="activeSection === 'about'" class="indicator"></span>
            </a>
  
            <a 
              href="#sectionReviews" 
              class="menu-item flex-1" 
              :class="{ 'active': activeSection === 'reviews' }"
              @click="scrollToSection('reviews')">
              {{ $t('navbar.feedback') }}
              <span v-if="activeSection === 'reviews'" class="indicator"></span>
            </a>
  
            <a 
              href="#sectionPricing" 
              class="menu-item flex-1" 
              :class="{ 'active': activeSection === 'pricing' }"
              @click="scrollToSection('pricing')">
              {{ $t('navbar.pricing') }}
              <span v-if="activeSection === 'pricing'" class="indicator"></span>
            </a>
  
            <RouterLink 
              :class="{ 'active': activeSection === 'faq' }"
              class="menu-item flex-1" 
              :to="{name: 'faq'}">
              {{ $t('navbar.faq') }}
              <span v-if="activeSection === 'faq'" class="indicator"></span>
            </RouterLink>
          </div>
        </RouterLink>
  
        <!-- Кнопки профиля или входа/регистрации -->
        <div class="flex-1 flex justify-end gap-2.5 z-50">
          <RouterLink v-if="isAuthenticated" :to="{ name: 'profile', params: { username: getUsername } }" v-slot="{ href }">
            <button class="text-white rounded-md px-4 py-1.5">{{ $t('navbar.profile') }}</button>
          </RouterLink>
          <template v-else>
            <button class="text-white rounded-md px-4 py-1.5" @click="$emit('open-login-popup')">{{ $t('navbar.login') }}</button>
            <button class="text-white bg-custom-gradient rounded-md px-4 py-1.5" @click="$emit('open-signup-popup')">{{ $t('navbar.signup') }}</button>
          </template>
        </div>

      </nav>
    </div>
</template>
  
<script setup lang="ts">
import { computed, ref, onMounted  } from 'vue';
import { useI18n } from 'vue-i18n';

import AuthService from '@/services/AuthService';

const isAuthenticated = computed(() => AuthService.isAuthenticated());
const getUsername = computed(() => AuthService.getUsername());

const props = defineProps<{
activeSection: string | null
}>();

const scrollToSection = (section: string) => {
const element = document.getElementById(`section${section.charAt(0).toUpperCase() + section.slice(1)}`);
if (element) {
    element.scrollIntoView({ behavior: 'smooth' });
}
};

const { locale } = useI18n();
const currentLanguage = ref<string>(localStorage.getItem('userLanguage') || 'en-US');
const switchLanguage = (lang: string) => {
    currentLanguage.value = lang;
    localStorage.setItem('userLanguage', lang);
    locale.value = currentLanguage.value;
};


onMounted(() => {
    currentLanguage.value = localStorage.getItem('userLanguage') || 'en-US';
});
</script>
  
<style scoped>
.menu-item {
  position: relative;
  padding: 0.5rem 1rem;
  text-decoration: none;
  color: white;
  cursor: pointer;
  white-space: nowrap; 
}

.indicator {
  display: block;
  position: absolute;
  bottom: -5px;
  left: 50%;
  transform: translateX(-50%);
  width: 6px; 
  height: 6px; 
  background-color: #A39BD6; 
  border-radius: 50%;
}

.menu-item.active {
  font-weight: bold;
}
</style>
  