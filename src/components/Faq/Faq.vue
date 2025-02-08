<template>
    <section class="p-8">
      <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div class="mb-24">
          <div class="text-center">
            <h1 class="custom-gradient-text-title text-6xl">{{ $t('faq.title') }}</h1>
          </div>
        </div>
  
        <div class="accordion-group space-y-10" data-accordion="default-accordion">
          <div
            v-for="faq in faqs"
            :key="faq.id"
            class="accordion py-8 px-6 border-bottom-custom-adventage transition-all duration-100 rounded-2xl"
            :class="{ 'space-y-5': faq.isOpen }"
          >
            <button
              @click="toggleFaq(faq.id)"
              class="accordion-toggle group inline-flex items-center justify-between leading-8 text-white w-full transition duration-100 text-left hover:custom-gradient-text-title-main font-bold"
              :class="{ 'custom-gradient-text-title-main': faq.isOpen }"
              :aria-controls="'basic-collapse-' + faq.id + '-with-arrow'"
            >
              <h5 class="text-3xl">{{ faq.question }}</h5>
  
              <svg
                class="text-gray-500 transition duration-100 group-hover:text-indigo-300"
                :class="{ 'rotate-180': faq.isOpen }"
                width="22"
                height="22"
                viewBox="0 0 22 22"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M16.5 8.25L12.4142 12.3358C11.7475 13.0025 11.4142 13.3358 11 13.3358C10.5858 13.3358 10.2525 13.0025 9.58579 12.3358L5.5 8.25"
                  stroke="currentColor"
                  stroke-width="1.6"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
              </svg>
            </button>
  
            <div
              :id="'basic-collapse-' + faq.id + '-with-arrow'"
              class="accordion-content w-full px-0 overflow-hidden transition-max-height duration-100 ease-in-out"
              :style="{ maxHeight: faq.isOpen ? '250px' : '0px' }"
              :aria-labelledby="'basic-heading-' + faq.id + '-with-arrow'"
            >
              <p class="text-xl text-white leading-6">{{ faq.answer }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </template>
  
  <script setup lang="ts">
  import { ref, computed } from 'vue';
  import { useI18n } from 'vue-i18n';
  
  const { t } = useI18n();
  
  // Хранение состояния открытия FAQ
  const faqState = ref({
    1: false,
    2: false,
    3: false,
    4: false,
  });
  
  // Computed для динамического обновления вопросов и ответов при смене языка
  const faqs = computed(() => [
    {
      id: 1,
      question: t('faq.q1'),
      answer: t('faq.a1'),
      isOpen: faqState.value[1],
    },
    {
      id: 2,
      question: t('faq.q2'),
      answer: t('faq.a2'),
      isOpen: faqState.value[2],
    },
    {
      id: 3,
      question: t('faq.q3'),
      answer: t('faq.a3'),
      isOpen: faqState.value[3],
    },
    {
      id: 4,
      question: t('faq.q4'),
      answer: t('faq.a4'),
      isOpen: faqState.value[4],
    },
  ]);
  
  // Функция для переключения состояния FAQ
  const toggleFaq = (faqId: number) => {
    // @ts-ignore
    faqState.value[faqId] = !faqState.value[faqId];
  };
  </script>
  