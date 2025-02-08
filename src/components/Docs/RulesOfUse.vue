<template>
    <div class="w-full max-w-7xl mx-auto p-8 space-y-16">
      <!-- Заголовок -->
      <div class="text-center">
        <h1 class="custom-gradient-text-title text-6xl">{{ $t('rules.title') }}</h1>
        <h2 class="faq-date-text text-2xl mt-2">{{ $t('rules.date') }}</h2>
      </div>
  
      <!-- Основной текст политики использования -->
      <div class="text-white space-y-6 leading-relaxed">
        <div>
          <h3 class="text-xl font-semibold mb-4">{{ $t('rules.section1.title') }}</h3>
          <p>{{ $t('rules.section1.text') }}</p>
          <ul class="list-disc list-inside">
            <li><strong>{{ $t('rules.section1.editingFiles') }}:</strong> {{ $t('rules.section1.editingFilesDesc') }}</li>
            <li><strong>{{ $t('rules.section1.hacking') }}:</strong> {{ $t('rules.section1.hackingDesc') }}</li>
            <li><strong>{{ $t('rules.section1.accountSharing') }}:</strong> {{ $t('rules.section1.accountSharingDesc') }}</li>
            <li><strong>{{ $t('rules.section1.fileDistribution') }}:</strong> {{ $t('rules.section1.fileDistributionDesc') }}</li>
          </ul>
        </div>
  
        <div>
          <h3 class="text-xl font-semibold mb-4">{{ $t('rules.section2.title') }}</h3>
          <p>{{ $t('rules.section2.text') }}</p>
        </div>
  
        <div>
          <h3 class="text-xl font-semibold mb-4">{{ $t('rules.section3.title') }}</h3>
          <p>{{ $t('rules.section3.text') }}</p>
        </div>
  
        <div>
          <h3 class="text-xl font-semibold mb-4">{{ $t('rules.section4.title') }}</h3>
          <p>{{ $t('rules.section4.text') }} support@drainwalk.tech.</p>
        </div>
      </div>
    </div>
</template>
  