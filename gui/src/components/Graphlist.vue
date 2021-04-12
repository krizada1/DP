<template>
  <v-card
    class="mx-auto"
    width="300"
  >
    <v-list
    rounded="True">
      <v-list-item>
            <v-list-item-title class="title">Graph choice</v-list-item-title>
      </v-list-item>

      <v-list-group
          no-action
          sub-group
        >
          <template v-slot:activator>
            <v-list-item-content>
              <v-list-item-title>Cycle time</v-list-item-title>
            </v-list-item-content>
          </template>

          <v-list-item
            v-for="([title, icon], i) in helpers"
            :key="i"
            link
          >
            <v-list-item-title v-text="title"></v-list-item-title>

            <v-list-item-icon>
              <v-icon v-text="icon"></v-icon>
            </v-list-item-icon>
          </v-list-item>
        </v-list-group>

        <v-list-group
          no-action
          sub-group
        >
          <template v-slot:activator>
            <v-list-item-content>
              <v-list-item-title>Oven 1</v-list-item-title>
            </v-list-item-content>
          </template>

          <v-list-item 
            v-for="([title, icon], i) in admins"
            :key="i"
            link
          >
            <v-list-item-title v-text="title"></v-list-item-title>

            <v-list-item-icon>
              <v-icon v-text="icon"></v-icon>
            </v-list-item-icon>
          </v-list-item>
        </v-list-group>

        <v-list-group
          no-action
          sub-group
        >
          <template v-slot:activator>
            <v-list-item-content>
              <v-list-item-title>Oven 2</v-list-item-title>
            </v-list-item-content>
          </template>

          <v-list-item
            v-for="([title, icon], i) in cruds"
            :key="i"
            link
          >
            <v-list-item-title v-text="title"></v-list-item-title>

            <v-list-item-icon>
              <v-icon v-text="icon"></v-icon>
            </v-list-item-icon>
          </v-list-item>
        </v-list-group>
      
    </v-list>
  </v-card>
</template>

<script>
  export default {
    data: () => ({
        helpers: [
        ['Unloading'],
      ],
      admins: [
        ['Temperature 1'],
      ],
      cruds: [
        ['Temperature 1'],
        ['Temperature 2'],
        ['Temperature 3'],
        ['Temperature 4'],
      ],
    }),
  }
</script>

<style scoped>
.title {
    font-size: 25px;
    font-weight: bold;
    background-color: black;
    color: white;
}

.v-list-item__content {
    text-align: left;
    font-weight: bold;
}
</style>