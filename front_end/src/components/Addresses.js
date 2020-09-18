import React, { useState, useEffect, useContext } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import Title from "./Title";
import { useHistory } from "react-router-dom";
import { UserContext } from "../contexts/UserContext";
import RowInList from './RowInList';
import classnames from 'classnames';

export default function Addresses ({ title }) {
  const { addressId, setAddressId } = useContext(UserContext);

  const [addresses, setAdrresses] = useState({
    addresses: [],
    isFetching: true,
  });
  const history = useHistory();

  const changeAddress = async (event) => {
    try {
      await setAddressId(parseInt(event.target.value));
    } catch (error) {
      console.log(error);
    }
  };
  const fetchAddresses = async () => {
    try {
      const response = await axios.get(`/api/address`, {
        headers: {
          Authorization: "JWT " + localStorage.getItem("access_token"),
          "Content-Type": "application/json",
          accept: "application/json",
        },
      });

      setAdrresses({ addresses: response.data, isFetching: false });
    } catch (error) {
      console.log(error);
    }
  };
  useEffect(() => {
    fetchAddresses();
  }, []);

  async function handleDelete (event) {
    event.preventDefault();
    let id = event.target.value;
    try {
      const response = await axios.delete(`api/address/${id}/`, {
        headers: {
          Authorization: "JWT " + localStorage.getItem("access_token"),
          "Content-Type": "application/json",
          accept: "application/json",
        },
      });

      fetchAddresses();
      return response;
    } catch (e) {
      console.log(e);
    }
  }

  const addressesGroup = () => {
    if (addresses.isFetching === true || addresses.addresses.length === 0) {
      return (
        <h3>You do not have any address, add address to make a purchase </h3>
      );
    }
    return (
      <div className="address-center">
        {addresses.addresses.map((item) => {
          return (
            <article
              key={item.address_id}
            >
              <h3 className={classnames({ 'active-shipping': addressId === item.address_id, 'diaactive-shipping ': addressId !== item.address_id})}>Shipping Address <div /></h3>
              <h6>
                <RowInList isInline title='Name:' content={item.name} />
              </h6>
              <RowInList isInline title='Country:' content={item.country} />
              <RowInList isInline title='Street:' content={item.street} />
              <RowInList isInline title='City:' content={item.city} />
              <RowInList isInline title='Post Code:' content={item.post_code} />
              <RowInList isInline title='Phone:' content={item.phone} />
              {addressId === item.address_id ? null : (
                <button
                  className="btn-primary"
                  value={item.address_id}
                  onClick={changeAddress}
                >
                  Order addrres
                </button>
              )}

              <button
                className="btn-primary"
                value={item.address_id}
                onClick={handleDelete}
              >
                Delete
              </button>
            </article>
          );
        })}
      </div>
    );
  };
  return (
    <div className="conteiner">
      <Title title={title} />
      <section>{addressesGroup()}</section>
      <div className="seperator" />
      <Link className="btn-primary btn-margin" to="/adresses-form">
        Add new address
      </Link>
    </div>
  );
}
