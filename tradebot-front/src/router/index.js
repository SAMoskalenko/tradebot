import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Login from '@/components/Login'
import Registration from '@/components/Registration'
import Account from '@/components/Account'
import Account_PUT from "@/components/Account_PUT";

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home
        },
        {
            path: '/login',
            name: 'login',
            component: Login
        },
        {
            path: '/registration',
            name: 'registration',
            component: Registration
        },
        {
            path: '/account',
            name: 'account',
            component: Account
        },
        {
            path: '/account_put',
            name: 'account_put',
            component: Account_PUT
        },
    ]
})
