import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
import ProfileView from '@/views/ProfileView.vue'
import DocView from '@/views/DocumentView.vue'
import FaqView from '@/views/FaqView.vue'

const routes = [
    { 
        path: '', 
        component: MainView,
        name: 'main'
    },

    { 
        path: '/profiles/:username', 
        component: ProfileView,
        name: 'profile',
        props: true
    },
    
    { 
        path: '/documents/:element', 
        component: DocView,
        name: 'documents',
        props: true
    },

    { 
        path: '/faq/', 
        component: FaqView,
        name: 'faq',
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router
