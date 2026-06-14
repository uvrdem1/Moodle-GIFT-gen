import axios from 'axios'

const API_URL =
  import.meta.env.VITE_API_URL ||
  '/api'

const api = axios.create({

  baseURL: API_URL
})

const refreshApi = axios.create({

  baseURL: API_URL
})

api.interceptors.request.use(

  (config) => {

    const token =
      localStorage.getItem('access')

    const isAuthPage =

      config.url?.includes(
        '/login/'
      ) ||

      config.url?.includes(
        '/register/'
      )

    if (
      token &&
      !isAuthPage
    ) {

      config.headers.Authorization =
        `Bearer ${token}`
    }

    return config
  }
)

api.interceptors.response.use(

  (response) => response,

  async (error) => {

    const originalRequest = error.config

    if (
      error.response?.status !== 401 ||
      originalRequest._retry ||
      originalRequest.url?.includes('/login/') ||
      originalRequest.url?.includes('/register/')
    ) {

      return Promise.reject(error)
    }

    originalRequest._retry = true

    const refresh =
      localStorage.getItem('refresh')

    if (!refresh) {

      localStorage.removeItem('access')

      return Promise.reject(error)
    }

    try {

      const response = await refreshApi.post(
        '/token/refresh/',
        {
          refresh
        }
      )

      localStorage.setItem(
        'access',
        response.data.access
      )

      originalRequest.headers.Authorization =
        `Bearer ${response.data.access}`

      return api(originalRequest)

    } catch (refreshError) {

      localStorage.removeItem('access')
      localStorage.removeItem('refresh')

      return Promise.reject(refreshError)
    }
  }
)

export default api
