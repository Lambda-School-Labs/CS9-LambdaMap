import React, { Component } from "react";
import JSnav from "../../nav/job-seeker/JSnav";
import Messenger from "../../messenger/Messenger";
import "./ClientLanding.css";
import amazon from "./amazon-logo.png";
import mark from "./0.png";
import marker from "./marker_icon.png";
import { get_listings, signout } from "../../../actions/index";
import { connect } from "react-redux";
import { GoClock } from "react-icons/go";
import { TiPin } from "react-icons/ti";

import JsMiniMap from "../../miniMap/JsMiniMap/JsMiniMap";
const Timestamp = require("react-timestamp");

class ClientLanding extends Component {
  constructor(props) {
    super(props);
    this.state = {
      clients: [],
      jobListing: [],
      color: "black"
    };
  }

  favorited = () => {
    if (this.state.color === "black") {
      this.setState({ color: "orange" });
    } else {
      this.setState({ color: "black" });
    }
  };

  componentDidMount = () => {
    this.props.get_listings();
  };

  render() {
    let user = JSON.parse(localStorage.getItem("user"));
    let companyListing = null;
    let favoritesListing = null;
    let favoritesListing2 = null;
    let favoritesListing3 = null;
    let favoritesListing4 = null;
    var randomCompany = this.props.jobListing.job_listings[
      Math.floor(Math.random() * this.props.jobListing.job_listings.length)
    ];
    var randomCompany2 = this.props.jobListing.job_listings[
      Math.floor(Math.random() * this.props.jobListing.job_listings.length)
    ];
    var randomCompany3 = this.props.jobListing.job_listings[
      Math.floor(Math.random() * this.props.jobListing.job_listings.length)
    ];
    var randomCompany4 = this.props.jobListing.job_listings[
      Math.floor(Math.random() * this.props.jobListing.job_listings.length)
    ];
    if (randomCompany) {
      companyListing = (
        <div className="feat-job">
          <img src={amazon} alt="company" />
          <div className="list-info">
            <div className="pinit">
              {/* <h3 className="jobloc">{randomCompany.company_name}</h3> */}
              <h3 className="jobloc">
                {randomCompany.city}, {randomCompany.state}
              </h3>{" "}
              <TiPin className={this.state.color} onClick={this.favorited} />
            </div>
            <h5 className="job">{randomCompany.jobListings[0].job_title}</h5>
            <p>{randomCompany.jobListings[0].job_desc}</p>
            <p className="post-time">
              <GoClock className="post-clock" />{" "}
              <Timestamp
                time={randomCompany.jobListings[0].posted_time}
                actualSeconds
              />
            </p>
          </div>
        </div>
      );
    }
    if (randomCompany2) {
      favoritesListing2 = (
        <div className="pinned-listing">
          <img src={amazon} alt="company" />
          <div className="list-info">
            <div className="pinit">
              <h3 className="jobloc">{randomCompany.city}, {randomCompany.state}</h3>
              <TiPin className="pin-icon" />
            </div>
              <h5 className="job">{randomCompany.jobListings[0].job_title}</h5>
            <p>{randomCompany.jobListings[0].job_desc}</p>
            <p className="post-time">
              <GoClock className="post-clock" />
              <Timestamp
                time={randomCompany.jobListings[0].posted_time}
                actualSeconds
              />
            </p>
          </div>
        </div>
      );
    }
    if (randomCompany3) {
      favoritesListing3 = (
        <div className="pinned-listing">
          <img src={amazon} alt="company" />
          <div className="list-info">
            <div className="pinit">
              <h3 className="jobloc">{randomCompany.city}, {randomCompany.state}</h3>
              <TiPin className="pin-icon" />
            </div>
              <h5 className="job">{randomCompany.jobListings[0].job_title}</h5>
            <p>{randomCompany.jobListings[0].job_desc}</p>
            <p className="post-time">
              <GoClock className="post-clock" />
              <Timestamp
                time={randomCompany.jobListings[0].posted_time}
                actualSeconds
              />
            </p>
          </div>
        </div>
      );
    }
    if (randomCompany4) {
      favoritesListing4 = (
        <div className="pinned-listing">
          <img src={amazon} alt="company" />
          <div className="list-info">
            <div className="pinit">
              <h3 className="jobloc">{randomCompany.city}, {randomCompany.state}</h3>
              <TiPin className="pin-icon" />
            </div>
              <h5 className="job">{randomCompany.jobListings[0].job_title}</h5>
            <p>{randomCompany.jobListings[0].job_desc}</p>
            <p className="post-time">
              <GoClock className="post-clock" />
              <Timestamp
                time={randomCompany.jobListings[0].posted_time}
                actualSeconds
              />
            </p>
          </div>
        </div>
      );
    }
    return (
      <div className="client">
        <JSnav />
        <JsMiniMap />
        <Messenger />
        <div className="landing-container">
          <div className="signout">
            <button
              className="signoutbutton"
              onClick={() => {
                this.props.signout(this.props.history);
              }}
            >
              Sign Out
            </button>
          </div>

          <div className="welcome-container">
            <img src={marker} className="profile-marker" alt="marker" />
            <img src={mark} className="mark" alt="user" />
            <h1>Welcome back, {user.first_name}.</h1>
          </div>
          {companyListing}
          <h3 className="pinned-title">Pinned Jobs:</h3>
          <div className="pinned-jobs">
            <div className="pinned-container">
              {favoritesListing}
              {favoritesListing2}
              {favoritesListing3}
              {favoritesListing4}
            </div>
          </div>
        </div>
      </div>
    );
  }
}

const mapStateToProps = state => {
  return {
    clients: state.clients,
    jobListing: state.jobListing,
    fetchingListings: state.fetchingListings,
    error: state.error
  };
};

export default connect(
  mapStateToProps,
  { get_listings, signout }
)(ClientLanding);
