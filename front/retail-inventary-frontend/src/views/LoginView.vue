<script setup>
import { ref } from "vue";
import { requestCode } from "../api/auth";

const phone = ref("");

const sendCode = async () => {
  try {
    await requestCode(phone.value);
    alert("Código enviado por WhatsApp");
  } catch (error) {
    alert("Error enviando código");
  }
};
</script>

<template>
  <div>
    <h2>Login con WhatsApp</h2>
    <input v-model="phone" placeholder="+573001234567" />
    <button @click="sendCode">Enviar Código</button>
  </div>
</template>
