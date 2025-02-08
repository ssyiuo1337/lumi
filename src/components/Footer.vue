<template>
    <footer class="absolute bottom-0 left-0 w-full py-4 px-8 flex justify-between items-center border-t border-gray-950 select-text">
      <div class="flex flex-col space-y-2 text-custom-white-adventage text-sm flex-1">
        <span>{{ $t('footer.contact_email') }} support@drainwalk.tech</span>
        <span>{{ $t('footer.copyright') }}</span>
        <span> 
          <a href="https://t.me/crypto_cheburah" target="_blank"> {{ $t('footer.design_by') }} </a> 
        </span>
      </div>
  
      <p class="flex text-custom-white-adventage">
        Захаров Максим Юрьевич | ИНН 623410373307
      </p>
  
      <div class="flex flex-col justify-between space-x-4 items-end flex-1">
        <div class="flex flex-col items-end">
          <RouterLink class="text-custom-white-adventage" :to="{ name: 'documents', params: { element: 'privacy_policy' } }">
            {{ $t('footer.privacy_policy') }}
          </RouterLink>
          <RouterLink class="text-custom-white-adventage" :to="{ name: 'documents', params: { element: 'terms_of_service' } }">
            {{ $t('footer.terms_of_service') }}
          </RouterLink>
          <RouterLink class="text-custom-white-adventage" :to="{ name: 'documents', params: { element: 'rules_of_use' } }">
            {{ $t('footer.rules_of_use') }}
          </RouterLink>
        </div>
        <div class="flex space-x-4">
          <a href="https://discord.gg/lumia_cc" target="_blank" class="text-2xl">
            <img src="../assets/img/icons/Footer/discord.png" alt="Discord Icon">
          </a>
          <a href="https://t.me/lumia_cc" target="_blank" class="text-2xl">
            <img src="../assets/img/icons/Footer/telegram.png" alt="Telegram Icon">
          </a>
        </div>
      </div>
    </footer>
  </template>
  
