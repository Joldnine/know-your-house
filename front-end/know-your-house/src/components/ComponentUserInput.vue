<template>
  <div>
    <el-form :model="form" ref="form" label-width="100px"
      class="demo-ruleForm">
      <el-form-item label="Address" prop="addr"
        :rules="[
          { required: true, message: 'Address is required'}
        ]"
      >
        <el-input v-model="form.addr" auto-complete="off"></el-input>
      </el-form-item>
      <el-form-item label="Size (sqf)" prop="size"
        :rules="[
          { required: true, message: 'Size is required'},
          { type: 'number', message: 'Size must be a number'}
        ]"
      >
        <el-input v-model.number="form.size"></el-input>
      </el-form-item>
      <el-form-item label="Level" prop="lvl"
        :rules="[
          { type: 'number', message: 'Level must be a number'}
        ]"
      >
        <el-input v-model.number="form.lvl"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm('form')">Submit</el-button>
        <el-button @click="resetForm('form')">Reset</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { getGeocode } from '@/api';

export default {
  name: 'ComponentUserInput',
  data() {
    return {
      form: {
        addr: '',
        size: '',
        lvl: '',
      },
    };
  },
  methods: {
    submitForm() {
      this.$store.commit('SET_PAGE_LOADING', true);
      this.$store.commit('SET_PAGE_CONTENT_LOADED', false);
      let loc = {};
      getGeocode(this.form.addr).then((result) => {
        loc = result.body;
        this.$store.commit('EDIT_USER_INPUT_ADDRESS', this.form.addr);
        this.$store.commit('EDIT_USER_INPUT_ADDRESS_LOC', JSON.parse(loc));
        this.$store.dispatch('requestNearbyPlaces', { loc }).then(() => {
          this.$store.commit('SET_PAGE_LOADING', false);
          this.$store.commit('SET_PAGE_CONTENT_LOADED', true);
        }).catch( () => {
          this.$store.commit('SET_PAGE_LOADING', false);
          this.$message('Failed to load data.');
        });
      }).catch( () => {
        this.$store.commit('SET_PAGE_LOADING', false);
        this.$message('Failed to load data.');
      });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
      this.$store.commit('RESET_USER_INPUT_ADDRESS');
      this.$store.commit('SET_PAGE_CONTENT_LOADED', false);
    },
  },
};
</script>

<style scoped>
</style>
