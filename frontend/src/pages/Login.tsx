import { useState } from 'react'

import { useNavigate } from 'react-router-dom'

import api from '../api'

export default function Login() {

  const navigate = useNavigate()

  const [username, setUsername] =
    useState('')

  const [password, setPassword] =
    useState('')

  const handleLogin = async () => {

    try {

      const response = await api.post(

        '/login/',

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

    } catch (error) {

      console.error(error)

      alert('Ошибка входа')
    }
  }

  return (

    <div className="min-h-screen flex items-center justify-center bg-slate-950 text-white">

      <div className="bg-slate-900 p-8 rounded-2xl w-full max-w-md">

        <h1 className="text-3xl font-bold mb-6">
          Вход
        </h1>

        <input
          type="text"
          placeholder="Логин"
          value={username}
          onChange={(e) =>
            setUsername(e.target.value)
          }
          className="w-full p-3 rounded mb-4 bg-slate-800"
        />

        <input
          type="password"
          placeholder="Пароль"
          value={password}
          onChange={(e) =>
            setPassword(e.target.value)
          }
          className="w-full p-3 rounded mb-4 bg-slate-800"
        />

        <button
          onClick={handleLogin}
          className="w-full bg-blue-600 p-3 rounded-xl hover:bg-blue-700"
        >
          Войти
        </button>

      </div>

    </div>
  )
}