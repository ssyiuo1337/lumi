<template>
    <div class=" w-full max-w-full h-full flex flex-col items-center justify-center gap-y-20 px-10 md:px-8">
        <div class="flex flex-col items-center justify-center gap-y-2 z-10 text-center">
            <span class="text-titles-color text-2xl px-4 py-1.5 rounded-3xl bg-custom-gradient-titles border-2 border-violet-300">{{ $t('feadback.title') }}</span>
            <h1 class="text-center text-6xl custom-gradient-text-title">{{ $t('feadback.title2') }}</h1>
        </div>

        <img src="@/assets/img/glow.png" alt="icon" class="absolute z-10 h-3/6 w-9/12 pointer-events-none"/>


        <div class="px-40 h-64 z-10">
            <Slider />
        </div>
    </div>
</template>

<script setup>
import Slider from '@/components/Reviews/Slider.vue';
</script>