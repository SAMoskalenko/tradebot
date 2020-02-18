<template>
    <div>
        <h1>
            Добро пожаловать в TradeBot Binance
        </h1>
        <button @click="goLogin">Вход</button>
        <button @click="goReg">Регистрация</button>
    </div>
</template>

<script>
    export default {
        name: "Home",
        methods:{
            goLogin(){
                this.$router.push({name:"login"})
            },
            goReg(){
                this.$router.push({name:"registration"})
            }
        }
    }
</script>

<style scoped>

</style>
