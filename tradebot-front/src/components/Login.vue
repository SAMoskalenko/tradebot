<template>
    <div>
        <input v-model="login" type="text" placeholder="Логин"/>
        <input v-model="password" type="password" placeholder="Пароль"/>
        <button @click="setLogin">Войти</button>
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
                        this.$router.push({name: "home"})
                    })
                    .catch(e => {
                        if (response.status === 400) {
                            alert("Логин или пароль не верен")
                        }
                    })
            },
        }
    }
</script>

<style scoped>
</style>
