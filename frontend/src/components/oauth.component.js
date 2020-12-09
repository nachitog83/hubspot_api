import React, { Component } from "react";

import OauthService from "../services/oauth.service";

export default class Oauth extends Component {
  constructor(props) {
    super(props);

    this.state = {
      content: ""
    };
  }

  componentDidMount() {
    OauthService.getPublicContent().then(
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
          <h3>HubSpot OAuth Authorization</h3>
        </header>
        <li className="list-group-item" key={this.state.content.msg}>
            <p><strong>Message: </strong> {this.state.content.msg} </p>
            <p><strong>Data: </strong>{this.state.content.data}</p>
        </li>
      </div>
    );
  }
}