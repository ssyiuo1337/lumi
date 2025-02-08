<template>
    <div class="w-full max-w-7xl mx-auto p-8 space-y-16">
      <!-- Заголовок -->
      <div class="text-center">
        <h1 class="custom-gradient-text-title text-6xl">{{ $t('privacy.title') }}</h1>
        <h2 class="faq-date-text text-2xl mt-2">{{ $t('privacy.date') }}</h2>
      </div>
  
      <!-- Основной текст политики конфиденциальности -->
      <div class="text-white space-y-6 leading-relaxed">
        <div>
          <h3 class="text-xl font-semibold mb-4">{{ $t('privacy.section1.title') }}</h3>
          <p>{{ $t('privacy.section1.text') }}</p>
        </div>
  
        <div>
          <h3 class="text-xl font-semibold mb-4">{{ $t('privacy.section2.title') }}</h3>
          <p>{{ $t('privacy.section2.text') }}</p>
          <ul class="list-disc list-inside">
            <li><strong>{{ $t('privacy.section2.name') }}:</strong> {{ $t('privacy.section2.nameDesc') }}</li>
            <li><strong>{{ $t('privacy.section2.email') }}:</strong> {{ $t('privacy.section2.emailDesc') }}</li>
          </ul>
        </div>
  
        <div>
          <h3 class="text-xl font-semibold mb-4">{{ $t('privacy.section3.title') }}</h3>
          <p>{{ $t('privacy.section3.text') }}</p>
          <ul class="list-disc list-inside">
            <li><strong>{{ $t('privacy.section3.communication') }}:</strong> {{ $t('privacy.section3.communicationDesc') }}</li>
            <li><strong>{{ $t('privacy.section3.improvement') }}:</strong> {{ $t('privacy.section3.improvementDesc') }}</li>
            <li><strong>{{ $t('privacy.section3.legal') }}:</strong> {{ $t('privacy.section3.legalDesc') }}</li>
          </ul>
        </div>
  
        <div>
          <h3 class="text-xl font-semibold mb-4">{{ $t('privacy.section4.title') }}</h3>
          <p>{{ $t('privacy.section4.text') }}</p>
        </div>
  
        <div>
          <h3 class="text-xl font-semibold mb-4">{{ $t('privacy.section5.title') }}</h3>
          <p>{{ $t('privacy.section5.text') }}</p>
        </div>
  
        <div>
          <h3 class="text-xl font-semibold mb-4">{{ $t('privacy.section6.title') }}</h3>
          <p>{{ $t('privacy.section6.text') }}</p>
        </div>
  
        <div>
          <h3 class="text-xl font-semibold mb-4">{{ $t('privacy.section7.title') }}</h3>
          <p>{{ $t('privacy.section7.text') }}</p>
          <ul class="list-disc list-inside">
            <li>{{ $t('privacy.section7.access') }}</li>
            <li>{{ $t('privacy.section7.delete') }}</li>
            <li>{{ $t('privacy.section7.withdraw') }} support@drainwalk.tech.</li>
          </ul>
        </div>
  
        <div>
          <h3 class="text-xl font-semibold mb-4">{{ $t('privacy.section8.title') }}</h3>
          <p>{{ $t('privacy.section8.text') }}</p>
        </div>
  
        <div>
          <h3 class="text-xl font-semibold mb-4">{{ $t('privacy.section9.title') }}</h3>
          <p>{{ $t('privacy.section9.text') }} support@drainwalk.tech.</p>
        </div>
      </div>
    </div>
  </template>
  