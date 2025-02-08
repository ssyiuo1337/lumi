<template>
    <div class="w-full max-w-7xl mx-auto p-8 space-y-16">
      <!-- Заголовок -->
      <div class="text-center">
        <h1 class="custom-gradient-text-title text-6xl">{{ $t('terms.title') }}</h1>
        <h2 class="faq-date-text text-2xl mt-2">{{ $t('terms.date') }}</h2>
      </div>
  
      <!-- Основной текст условий использования -->
      <div class="text-white space-y-6 leading-relaxed">
        <div>
          <h3 class="text-xl font-semibold mb-4">{{ $t('terms.section1.title') }}</h3>
          <p>{{ $t('terms.section1.text') }}</p>
        </div>
  
        <div>
          <h3 class="text-xl font-semibold mb-4">{{ $t('terms.section2.title') }}</h3>
          <p>{{ $t('terms.section2.text') }}</p>
        </div>
  
        <div>
          <h3 class="text-xl font-semibold mb-4">{{ $t('terms.section3.title') }}</h3>
          <p>{{ $t('terms.section3.text') }}</p>
          <ul class="list-disc list-inside">
            <li><strong>{{ $t('terms.section3.respectLaw') }}:</strong> {{ $t('terms.section3.respectLawDesc') }}</li>
            <li><strong>{{ $t('terms.section3.respectOthers') }}:</strong> {{ $t('terms.section3.respectOthersDesc') }}</li>
            <li><strong>{{ $t('terms.section3.respectServices') }}:</strong> {{ $t('terms.section3.respectServicesDesc') }}</li>
          </ul>
        </div>
  
        <div>
          <h3 class="text-xl font-semibold mb-4">{{ $t('terms.section4.title') }}</h3>
          <p>{{ $t('terms.section4.text') }}  support@drainwalk.tech.</p>
        </div>
  
        <div>
          <h3 class="text-xl font-semibold mb-4">{{ $t('terms.section5.title') }}</h3>
          <p><strong>{{ $t('terms.section5.payment') }}:</strong> {{ $t('terms.section5.paymentDesc') }}</p>
          <p><strong>{{ $t('terms.section5.refunds') }}:</strong> {{ $t('terms.section5.refundsDesc') }}</p>
        </div>
  
        <div>
          <h3 class="text-xl font-semibold mb-4">{{ $t('terms.section6.title') }}</h3>
          <p>{{ $t('terms.section6.text') }}</p>
        </div>
  
        <div>
          <h3 class="text-xl font-semibold mb-4">{{ $t('terms.section7.title') }}</h3>
          <p>{{ $t('terms.section7.text') }}</p>
        </div>
  
        <div>
          <h3 class="text-xl font-semibold mb-4">{{ $t('terms.section8.title') }}</h3>
          <p>{{ $t('terms.section8.text') }}</p>
        </div>
  
        <div>
          <h3 class="text-xl font-semibold mb-4">{{ $t('terms.section9.title') }}</h3>
          <p>{{ $t('terms.section9.text') }}  support@drainwalk.tech.</p>
        </div>
      </div>
    </div>
  </template>
  