import React, { Component } from "react";

import DealService from "../services/deal.service";

export default class UpdateDeal extends Component {
  constructor(props) {
    super(props);

    this.state = {
      content: ""
    };
  }

  componentDidMount() {
    DealService.updateDeals().then(
      response => {
        this.setState({
          content: response
        });
      },
      error => {
        this.setState({
          content:
            (error.response && error.response.data) ||
            error.message ||
            error.toString()
        });
      }
    );
  }
  render() {
    return (
      <div className="container">
        <header className="jumbotron">
          <h3 class="text-center">RETRIEVE DEALS FROM HUBSPOT</h3>
        </header>
        <li className="list-group-item" key={this.state.content.success}>
            <p><strong>Success: </strong>{this.state.content.success} </p>
        </li>
      </div>
    );
  }
}
