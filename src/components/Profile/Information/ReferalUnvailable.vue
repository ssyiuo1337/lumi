<template>
    <div class="relative flex-grow space-y-5">
        <div class="bg-custom-black-adventage border-bottom-custom-adventage rounded-xl flex flex-col p-5 w-full">

            <div class="flex flex-wrap justify-between blur-[11px]">
                <div class="flex flex-row text-xl gap-x-2 items-center">
                    <img src="@/assets/img/icons/Profile/Info/Refferal.svg" class="w-6 h-6">
                    <span class="text-white">Your Refferal Code</span>
                </div>

                <div class="text-xl">
                    <span class="custom-gradient-text-title-main">Unavailable</span>
                </div>
            </div>

            <div class="flex flex-wrap justify-between gap-y-2 blur-[11px]">
                <div class="flex flex-row text-xl gap-x-2 items-center">
                    <img src="@/assets/img/icons/Profile/Info/RefferalNum.svg" class="w-6 h-6">
                    <span class="text-white">Number Of Refferals</span>
                </div>

                <div class="text-xl">
                    <span class="custom-gradient-text-title-main">Unavailable</span>
                </div>
            </div>

            <div class="flex flex-wrap justify-between gap-y-2 blur-[11px]">
                <div class="flex flex-row text-xl gap-x-2 items-center">
                    <img src="@/assets/img/icons/Profile/Info/RefferalBonus.svg" class="w-6 h-6">
                    <span class="text-white">Refferal Bonus Earned</span>
                </div>

                <div class="text-xl">
                    <span class="custom-gradient-text-title-main">Unavailable</span>
                </div>
            </div>
        </div>

        <div class="absolute inset-0 flex flex-col justify-center items-center text-[#858588]">
            <span class="text-xl">Refferal System Unavailable</span>
            <span class="text-xl">Click the link below to get started:</span>
            <a class="text-xl" href="https://t.me/drainwalkbot" target="_blank">t.me/drainwalkbot</a>
        </div>
    </div>
</template>

<script setup lang="ts">
</script>
