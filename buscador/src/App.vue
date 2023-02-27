<script setup>
import { ref } from 'vue';

const text = ref("");
const listaLinks = ref([]);

const buscar = async (e) => {
  e.preventDefault();
  const res = await fetch("http://127.0.0.1:5000/",{
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    mode: 'cors', // no-cors, *cors, same-origin
    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    credentials: 'same-origin', // include, *same-origin, omit
    headers: {
      'Content-Type': 'application/json'
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
    redirect: 'follow', // manual, *follow, error
    referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
    body: JSON.stringify({"request":text.value}) // body data type must match "Content-Type" header
  });
  const respuesta = await res.json() 
  listaLinks.value = respuesta['data']
  console.log(listaLinks.value);
} ;

</script>

<template>
  <div class="container">
    <div id="barraBusqueda" class="row col">
      <h1 class="m-auto col-12 text-center mt-3">PABLITOBANANIN</h1>
      <form action="" class="col-6 m-auto mt-3">
        <div class="input-group">
          <input type="text" name="request" id="buscador" class="form-control" v-model="text" placeholder="Buscar en internet"/>
          <button type="submit" class="input-group-text" @click="buscar"><i class="bi bi-search"></i></button>
        </div>
      </form>
    </div>
    <div id="resultados" class="mt-4">
      <div class="card row col-md-6 mb-2" v-for="(link,i) in listaLinks" :key="i">
        <a :href="link._id" class="h3 text-decoration-none ">{{link["title"]}}</a>
        <a :href="link._id">{{link["_id"]}}</a>
      </div>
    </div>
  </div>
</template>

<style scoped>
@import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.1/font/bootstrap-icons.css");
</style>
