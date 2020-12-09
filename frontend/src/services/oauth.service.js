import axios from 'axios';
import authHeader from './auth-header';

const API_URL = 'http://localhost:5000/api/oauth/';

class OauthService {
  getPublicContent() {
    return axios
      .get(API_URL + 'authorize', { headers: authHeader() })
      .then(response => {
        return response.data;
      });
  }
}

export default new OauthService();