<template>
    <div class="review flex flex-col items-center justify-center p-4 bg-custom-black-adventage rounded-xl shadow-lg lg:w-[600px] w-[300px] min-h-[150px] text-custom-white-adventage bg-opacity-50 px-6 py-[19.2px] gap-y-4 border-bottom-custom-adventage z-50 relative">
        <div class="flex flex-row w-full gap-x-4">
            <img src="@/assets/img/ReviewsAvatars/test.jpeg" alt="User Avatar" class="w-10 h-10 rounded-full ring-2 ring-[#D4CDFF] ring-offset-4 ring-offset-[#09090D] shadow-custom">
            <div class="flex flex-row items-center">
                <img src="@/assets/img/star.svg" class="w-[19.2px] h-[19.2px]">
                <img src="@/assets/img/star.svg" class="w-[19.2px] h-[19.2px]">
                <img src="@/assets/img/star.svg" class="w-[19.2px] h-[19.2px]">
                <img src="@/assets/img/star.svg" class="w-[19.2px] h-[19.2px]">
                <img src="@/assets/img/star.svg" class="w-[19.2px] h-[19.2px]">
            </div>
        </div>
        <p class="font-normal text-xl">{{ review.text }}</p>

        <!-- Poloska images on the right -->
        <div class="absolute right-0 top-0 h-full flex flex-row items-start	object-cover">
            <img src="@/assets/img/poloska.png" class="h-full -mr-3">
            <img src="@/assets/img/poloska.png" class="h-full mr-5">
        </div>
    </div>
</template>

<script lang="ts" setup>
const props = defineProps<{
  review: {
    text: string;
    avatar: string;
  };
}>();
</script>