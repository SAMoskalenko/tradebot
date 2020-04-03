<template>
    <div>
        <h1>
            Личный кабинет
        </h1>
        <div>
            <h4>
                <span>Имя пользователя</span>
                <input v-model="user_name" type="text" placeholder="Имя пользователя"/>
            </h4>
            <h4>
                <span>Ключ Binance</span>
                <input v-model="binance_key" type="text" placeholder="Ключ Binance"/>
            </h4>
            <h4>
                <span>Секретный ключ Binance</span>
                <input v-model="binance_secret" type="text" placeholder="Секретный ключ Binance"/>
            </h4>
            <h4>
                <span>CHAT ID в Телеграм</span>
                <input v-model="chat_id" type="number" placeholder="CHAT ID в Телеграм"/>
            </h4>
            <button @click="setAccount">Внести изменения</button>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import config from "../config";

    export default {
        name: "Account_PUT",
        data() {
            return {
                user_name: '',
                binance_key: '',
                binance_secret: '',
                chat_id: '',
            }
        },
        methods: {
            setAccount() {
                const token = localStorage.getItem('user-token')
                axios.put(`${config.apiUrl}/accounts/1/`,
                    {
                        name: this.user_name,
                        binance_key: this.binance_key,
                        binance_secret: this.binance_secret,
                        chat_id: this.chat_id
                    },
                    {headers: {'Authorization': "Bearer " + token}})
                    .then(response => {
                        this.$router.push({name: "account"})
                    })
                    .catch(e => {
                        alert("Проверьте правильность данных")
                    })
            }
        }
    }
</script>

<style scoped>

</style>
