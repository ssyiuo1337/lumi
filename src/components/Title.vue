<template>

    <img src="@/assets/img/Dots/TitleDots.png" alt="" class="absolute pointer-events-none">

    <div class="  w-full max-w-full h-full flex flex-col items-center justify-center gap-y-2">

        <h1 class="text-center text-white text-6xl">{{ $t('title.first') }}</h1>
        <img src="@/assets/img/glow.png" class="absolute z-10 pointer-events-none">
        <h1 class="text-center text-6xl custom-gradient-text-title-main ">{{ $t('title.second') }}</h1>

        <button class="flex items-center text-white bg-custom-gradient rounded-md px-4 py-1.5 text-2xl shadow-custom"
            @click="scrollToSection('pricing')">
            {{ $t('title.button') }}
            <img src="@/assets/img/icons/buyico.svg" alt="icon" class="ml-2 w-6 h-6 pointer-events-none">
        </button>

    </div>
</template>
    
<script setup lang="ts">

const scrollToSection = (section: string) => {
    const element = document.getElementById(`section${section.charAt(0).toUpperCase() + section.slice(1)}`)
    if (element) {
        element.scrollIntoView({ behavior: 'smooth' })
    }
}
</script>
    