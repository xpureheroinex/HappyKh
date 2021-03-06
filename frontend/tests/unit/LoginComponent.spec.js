import { shallowMount, createLocalVue } from '@vue/test-utils';
import Vuetify from 'vuetify';
import LoginComponent from '../../src/components/LoginComponent.vue';

const expect = require('chai').expect;

const localVue = createLocalVue();
localVue.use(Vuetify);

describe('LoginComonent', () => {
  const wrapper = shallowMount(LoginComponent, { localVue });

  it('has default userEmail', () => {
    expect(LoginComponent.data()).to.have.property('userEmail');
  });

  it('has default userPassword', () => {
    expect(LoginComponent.data()).to.have.property('userPassword');
  });

  it('contains userEmail input field', () => {
    expect(wrapper.contains('[name="userEmail"]')).to.be.equal(true);
  });

  it('contains userPassword input field', () => {
    expect(wrapper.contains('[name="userPassword"]')).to.be.equal(true);
  });

  it('contains button for submitting user credentials', () => {
    expect(wrapper.contains('[class="btn-submit"]')).to.be.equal(true);
  });
});
