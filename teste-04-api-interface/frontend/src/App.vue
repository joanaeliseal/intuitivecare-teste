<script setup>
import { ref } from 'vue'
import OperadoraBusca from './components/OperadoraBusca.vue'
import OperadoraLista from './components/OperadoraLista.vue'

const resultados = ref([])
const buscou = ref(false)

const realizarBusca = async (termo) => {
  try {
    const res = await fetch(`http://localhost:8000/buscar?termo=${termo}`)
    resultados.value = await res.json()
    buscou.value = true
  } catch (error) {
    console.error('Erro ao buscar operadoras:', error)
    resultados.value = []
    buscou.value = true
  }
}
</script>

<template>
  <div class="min-h-screen bg-gray-50 font-sans">
    <header class="bg-[#C8A4F4] text-white py-6 shadow-md">
      <h1 class="text-center text-2xl font-bold tracking-wide">
        Buscador de Operadoras - IntuitiveCare
      </h1>
    </header>

    <main class="py-6">
      <OperadoraBusca @buscar="realizarBusca" />
      <OperadoraLista :operadoras="resultados" :buscou="buscou" />
    </main>
  </div>
</template>

<style>
body {
  font-family: 'Poppins', sans-serif;
}
</style>

