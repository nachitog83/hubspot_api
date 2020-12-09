import axios from 'axios';
import authHeader from './auth-header';

const API_URL = 'http://localhost:5000/api/deals/';

class DealService {
  updateDeals() {
    return axios
      .get(API_URL + 'update', { headers: authHeader() })
      .then(response => {
        return response.data;
      });
  };
  showDeals() {
    return axios
      .get(API_URL + 'show', { headers: authHeader() })
      .then(response => {
        return response.data;
      });
  }
}

export default new DealService();