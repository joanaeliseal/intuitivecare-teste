<template>
  <section class="px-4 max-w-6xl mx-auto">
    <div
      v-if="buscou && operadoras.length === 0"
      class="text-center text-gray-500 mt-8"
    >
      Nenhuma operadora encontrada.
    </div>

    <div
      v-else
      class="grid gap-6 mt-6 sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3"
    >
      <div
        v-for="operadora in operadoras"
        :key="operadora.registro_ans"
        class="bg-white p-6 rounded-xl shadow hover:shadow-lg transition duration-300"
      >
        <h3 class="text-lg font-semibold text-gray-800 mb-2">
          {{ operadora.Nome_Fantasia || 'Nome fantasia não informado' }}
        </h3>
        <p class="text-sm text-gray-600">
          Registro ANS: <strong>{{ operadora.Registro_ANS}}</strong>
        </p>
      </div>
    </div>
  </section>
</template>

<script setup>
defineProps({
  operadoras: Array,
  buscou: Boolean,
})
</script>
