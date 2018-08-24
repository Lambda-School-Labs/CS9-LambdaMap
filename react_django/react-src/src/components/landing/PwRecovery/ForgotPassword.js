import React, { Component } from 'react'
import { isError } from 'util';


const apiUrl = "http://127.0.0.1:8000/api/";
export default class ForgotPassword extends Component {
  constructor(){
    super();
    this.state = {
      clients: [],
      hire_partners: [],
      client: false,
      hire_partner: false,
      answer_attempt: ''
    }
  }
  componentDidMount() {
    axios.get(`${apiUrl}`/clients)
    .then(res => {
      this.setState({clients: res.data})
      console.log('Clients fetched!')
    })
    .catch(err => {
      console.log('Whoops, there was an error', err)
      
    })
    axios.get(`${apiUrl}`/hire-partners)
    .then(res => {
      this.setState({hire_partners: res.data})
      console.log('Hire Partners fetched!')
    })
    .catch(err => {
    })
  }

  handleReset = () => {
    this.setState({answer_attempt: ''})
  }
  handleTextChange = event => {
    event.preventDefault();
    this.setState({[event.target.name]: event.target.value})
  }
  handleRadioChange = event => {
    event.preventDefault();
    if(event.target.name === "client") {
      this.setState({client:true, hire_partner:false})
    }
    else if(event.target.name === "hire_partner") {
      this.setState({client:false, hire_partner:true})
    }
  }
  handleSubmit = () => {
    const {
      answer_attempt,
      client,
      business
    } = this.state
    if(client){
      axios.post(`${apiUrl}`/)
    }
    else if(hire_partner){

    }
    else {
      this.handleReset();
      alert("couldn't complete request, please try again")
    }
  }
  render() {
    return (
      <div>
        <h1>
          Forgot your password? We can help you out with that!
        </h1>
        <input type='radio' value={this.state.client} onChange={this.handleRadioChange} name='client'/>
        Client Account
        <input type='radio' value={this.state.business} onChange={this.handleRadioChange} name='business'/>
        Business Account
       {this.state.client
       ?
       <div>  
       <h1>Please answer the security question below:</h1>
       <h1>{this.state.clients._id.security_question}</h1>
       <form onSubmit={this.handleSubmit}>
       <input type="text" value={this.state.answer_attempt} onChange={this.handleTextChange} name={this.state.answer_attempt} placeholder="Please enter you security question's answer"/>
       <button type="submit">Submit</button>
        <button type="button" onClick={this.handleReset}>Cancel</button>
        </form>
        </div> 
       :
       null
      }
      {this.state.hire_partner 
        ?
        <div>
        <h1>
        Please answer your security question:
        {this.state.hire_partner._id.security_question}
        </h1>
        <form>
        <input type="text" value={this.state.answer_attempt} onChange={this.handleTextChange} placeholder="Please enter you security question's answer"/>
        <button type="submit">Submit</button>
        <button type="button" onClick={this.handleReset}> Cancel </button>
        </form>
        </div>
        :
        null
      }
      </div>
    )
  }
}
