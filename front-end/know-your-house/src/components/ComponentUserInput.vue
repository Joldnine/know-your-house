<template>
  <div>
    <el-form :model="form" ref="form" label-width="100px"
      class="demo-ruleForm">
      <el-row>
        <el-form-item label="Address" prop="addr"
          :rules="[
            { required: true, message: 'Address is required'}
          ]">
          <el-input v-model="form.addr" auto-complete="off"></el-input>
        </el-form-item>
      </el-row>
      <el-row>
        <el-col :span="12">
          <el-form-item label="Flat type" prop="flatType"
            :rules="[
              { required: true, message: 'Flat type is required'}
            ]">
            <el-select v-model="form.flatType" placeholde="Select" style="width:100%;">
              <el-option
                v-for="item in flatTypeOpts"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          </el-form-item>
        </el-col>
        <el-col :span="12">
          <el-form-item label="Size (sqm)" prop="size"
            :rules="[
              { required: true, message: 'Size is required'},
              { type: 'number', message: 'Size must be a number'}
            ]">
            <el-input v-model.number="form.size"></el-input>
          </el-form-item>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="12">
          <el-form-item label="Floor" prop="floor"
            :rules="[
              { type: 'number', message: 'Floor must be a number'}
            ]">
            <el-input-number v-model="form.floor" :min="1" :max="100" style="width:100%;"></el-input-number>
          </el-form-item>
        </el-col>
        <el-col :span="12">
          <el-form-item label="House age" prop="age"
            :rules="[
              { type: 'number', message: 'House age must be a number'}
            ]">
            <el-input-number v-model="form.age" :min="0" :max="100" style="width:100%;"></el-input-number>
          </el-form-item>
        </el-col>
      </el-row>
      <el-row>
        <el-form-item>
          <el-button type="primary" @click="submitForm('form')">Submit</el-button>
          <el-button @click="resetForm('form')">Reset</el-button>
        </el-form-item>
      </el-row>
    </el-form>
  </div>
</template>

<script>
import { getGeocode } from '@/api';

export default {
  name: 'ComponentUserInput',
  data() {
    return {
      flatTypeOpts: [{
        value: '3 Room',
        label: '3 Room',
      }, {
        value: '4 Room',
        label: '4 Room',
      }, {
        value: '5 Room',
        label: '5 Room',
      },],
      form: {
        addr: '',
        flatType: '',
        size: '',
        floor: '',
        age: '',
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
