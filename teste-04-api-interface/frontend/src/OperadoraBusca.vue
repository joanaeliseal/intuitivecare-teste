<template>
    <div class="busca-container">
      <h1>Buscar Operadoras</h1>
      <input v-model="termo" placeholder="Digite o nome da operadora" />
      <button @click="buscar">Buscar</button>
  
      <ul v-if="resultados.length">
        <li v-for="(item, index) in resultados" :key="index">
          {{ item.Nome_Fantasia || item.Razao_Social }} - Registro ANS: {{ item.Registro_ANS }}
        </li>
      </ul>
      <p v-else-if="buscou">Nenhum resultado encontrado.</p>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  
  const termo = ref('')
  const resultados = ref([])
  const buscou = ref(false)
  
  async function buscar() {
    try {
      const response = await fetch(`http://127.0.0.1:8000/buscar?termo=${termo.value}`)
      const data = await response.json()
      resultados.value = data
      buscou.value = true
    } catch (error) {
      console.error('Erro na busca:', error)
    }
  }
  </script>
  
  <style scoped>
  .busca-container {
    max-width: 600px;
    margin: 2rem auto;
    text-align: center;
  }
  input {
    padding: 8px;
    width: 300px;
    margin-right: 10px;
  }
  button {
    padding: 8px 16px;
  }
  li {
    text-align: left;
    margin-top: 10px;
  }
  </style>
  