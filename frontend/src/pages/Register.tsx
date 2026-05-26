import { useState } from 'react'

import { useNavigate } from 'react-router-dom'

import api from '../api'


export default function Register() {

  const navigate = useNavigate()

  const [username, setUsername] =
    useState('')

  const [password, setPassword] =
    useState('')

  const [errorMessage, setErrorMessage] =
    useState('')


  const handleRegister = async () => {

    try {

      setErrorMessage('')

      const response = await api.post(

        '/register/',

        {
          username,
          password
        }
      )

      localStorage.setItem(

        'access',

        response.data.access
      )

      localStorage.setItem(

        'refresh',

        response.data.refresh
      )

      navigate('/')

    } catch (error: any) {

      console.log(
        error.response?.data
      )

      if (
        error.response?.data?.username
      ) {

        setErrorMessage(
          error.response.data.username[0]
        )

      } else if (
        error.response?.data?.password
      ) {

        setErrorMessage(
          error.response.data.password[0]
        )

      } else if (
        error.response?.data?.detail
      ) {

        setErrorMessage(
          error.response.data.detail
        )

      } else {

        setErrorMessage(
          'Ошибка регистрации'
        )
      }
    }
  }


  return (

    <div className="min-h-screen flex items-center justify-center bg-slate-950 text-white">

      <div className="bg-slate-900 p-8 rounded-2xl w-full max-w-md">

        <h1 className="text-3xl font-bold mb-6">
          Регистрация
        </h1>


        {
          errorMessage && (

            <div className="bg-red-500/20 border border-red-500 text-red-300 p-3 rounded-xl mb-4">

              {errorMessage}

            </div>
          )
        }


        <input
          type="text"
          placeholder="Логин"
          value={username}
          onChange={(e) =>
            setUsername(e.target.value)
          }
          className="w-full p-3 rounded mb-4 bg-slate-800 outline-none"
        />


        <input
          type="password"
          placeholder="Пароль"
          value={password}
          onChange={(e) =>
            setPassword(e.target.value)
          }
          className="w-full p-3 rounded mb-4 bg-slate-800 outline-none"
        />


        <button
          onClick={handleRegister}
          className="w-full bg-green-600 p-3 rounded-xl hover:bg-green-700 transition-all"
        >
          Зарегистрироваться
        </button>

      </div>

    </div>
  )
}