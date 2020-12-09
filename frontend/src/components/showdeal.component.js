import React, { Component } from "react";

import DealService from "../services/deal.service";

export default class ShowDeal extends Component {
  constructor(props) {
    super(props);

    this.state = {
      json: []
    };
  }

  componentDidMount() {
    DealService.showDeals().then(
      response => {
        console.log(response)
        this.setState({
          json: response
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
          <h3 class="text-center">SHOW IMPORTED DEALS</h3>
        </header>
        <table class="table">
          <thead>
              <th scope="col">Deal ID</th>
              <th scope="col">Deal Name</th>
              <th scope="col">Deal Stage</th>
              <th scope="col">Deal Type</th>
              <th scope="col">Amount</th>
              <th scope="col">Close Date</th>
          </thead>
          <tbody>
              {this.state.json.map((data, i) => {
                  return (
                      <tr key={i}>
                          <td scope="row">{data.dealid}</td>
                          <td scope="row">{data.dealname}</td>
                          <td scope="row">{data.dealstage}</td>
                          <td scope="row">{data.dealtype}</td>
                          <td scope="row">{data.amount}</td>
                          <td scope="row">{data.closedate}</td>
                      </tr>
                      )
                  }
              )
                }
          </tbody>
        </table>
      </div>
    );
  }
}