<template>
    <div>
        <input v-model="login" type="text" placeholder="Логин"/>
        <input v-model="password" type="password" placeholder="Пароль"/>
        <button @click="setLogin">Войти</button>
        <button @click="goReg">Регистрация</button>
        <button @click="goHome">Домой</button>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: "Login",
        data() {
            return {
                login: '',
                password: '',
            }
        },
        methods: {
            setLogin() {
                axios.post(
                    "http://127.0.0.1:8000/auth/login/",
                    {
                        username: this.login,
                        password: this.password
                    })
                    .then(response => {
                        alert("Спасибо что Вы с нами")
                        const token = response.data.token
                        console.log(token)
                        localStorage.setItem('user-token', token)
                        this.$router.push({name: "account"})
                    })
                    .catch(e => {
                        localStorage.removeItem('user-token')
                        alert("Логин или пароль не верен")
                    })
            },
            goHome() {
                this.$router.push({name: "home"})
            },
            goReg() {
                this.$router.push({name: "registration"})
            },
        }
    }
</script>

<style scoped>
</style>
