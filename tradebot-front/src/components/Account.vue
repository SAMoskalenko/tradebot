<template>
    <div>
        <h1>
            Личный кабинет
        </h1>
        <div>
            <h4>
                <span>Имя пользователя</span>
                <span>{{account['name']}}</span>
            </h4>
            <h4>
                <span>Ключ Binance</span>
                <span>{{account['binance_key']}}</span>
            </h4>
            <h4>
                <span>Секретный ключ Binance</span>
                <span>{{account['binance_secret']}}</span>
            </h4>
            <h4>
                <span>CHAT ID в Телеграм</span>
                <span>{{account['chat_id']}}</span>
            </h4>
            <h4>
                <span>Баланс</span>
                <span>{{account['balance']}}</span>
            </h4>
            <button @click="goAccountPUT">Внести изменения</button>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import config from "../config";

    export default {
        name: "Account",
        data: () => ({
            account: {}
        }),
        methods: {
            goAccountPUT() {
                this.$router.push({name: "account_put"})
            },
        },
        created() {
            const token = localStorage.getItem('user-token')
            axios.get(`${config.apiUrl}/accounts/`, {headers: {'Authorization': "Bearer " + token}})
                .then(response => {
                    this.account = response.data[0]
                })
                .catch(e => {
                    alert("Невозможно получить данные")
                })
        }
    }
</script>

<style scoped>

</style>
