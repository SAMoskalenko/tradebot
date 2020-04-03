<template>
    <div>
        <input v-model="login" type="text" placeholder="Логин"/>
        <input v-model="password1" type="password" placeholder="Пароль"/>
        <input v-model="password2" type="password" placeholder="Пароль"/>
        <button @click="setReg">Зарегистрироваться</button>
        <button @click="goLogin">Вход</button>
        <button @click="goHome">Домой</button>
    </div>
</template>

<script>
    import axios from 'axios'
    import config from "../config";

    export default {
        name: "Registration",
        data() {
            return {
                login: '',
                password1: '',
                password2: '',
            }
        },
        methods: {
            goLogin() {
                this.$router.push({name: "login"})
            },
            goHome() {
                this.$router.push({name: "home"})
            },
            setReg() {
                axios.post(
                    `${config.apiUrl}/auth/registration/`,
                    {
                        username: this.login,
                        password1: this.password1,
                        password2: this.password2
                    })
                    .then(response => {
                        alert("Спасибо что Вы с нами")
                        sessionStorage.this.$router.push({name: "account"})
                    })
                    .catch(e => {
                        alert("Невозможно зарегистрировать")
                    })
            },
        }
    }
</script>

<style scoped>
</style>
