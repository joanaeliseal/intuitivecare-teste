<template>
  <div class="flex justify-center gap-4 mb-6">
    <input
      v-model="termo"
      @keyup.enter="emitirBusca"
      type="text"
      placeholder="Digite o nome da operadora"
      class="w-80 px-4 py-2 rounded border border-gray-300 shadow-sm focus:outline-none focus:ring-2 focus:ring-primary"
    />
    <button
    @click="emitirBusca"
    style="background-color: #9851EF"
    class="text-white px-4 py-2 rounded hover:brightness-110 transition"
  > 
    Buscar
    </button>

  </div>
</template>

<script setup>
import { ref } from 'vue'

const termo = ref('')

const emitirBusca = () => {
  if (termo.value.trim().length >= 2) {
    emit('buscar', termo.value)
  }
}

const emit = defineEmits(['buscar'])
</script>
