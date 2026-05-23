import { motion } from 'framer-motion'

import {
  FileText,
  Download,
  Copy,
} from 'lucide-react'


interface QuestionsPreviewProps {

  giftResult: string

  setGiftResult: (
    value: string
  ) => void

  copyGift: () => void

  downloadGift: () => void
}


export default function QuestionsPreview({

  giftResult,
  setGiftResult,

  copyGift,
  downloadGift

}: QuestionsPreviewProps) {

  return (

    <motion.div
      whileHover={{ scale: 1.01 }}
      className="backdrop-blur-xl bg-white/10 border border-white/10 rounded-3xl p-8 shadow-2xl"
    >

      <div className="flex justify-between items-center mb-6">

        <div className="flex items-center gap-3">

          <FileText className="text-green-400" />

          <h2 className="text-2xl font-semibold">
            Сгенерированные вопросы
          </h2>

        </div>


        <div className="flex gap-3">

          {
            giftResult && (

              <motion.button
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                onClick={copyGift}
                className="bg-slate-800 hover:bg-slate-700 p-3 rounded-xl"
              >

                <Copy size={20} />

              </motion.button>
            )
          }


          {
            giftResult && (

              <motion.button
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                onClick={downloadGift}
                className="bg-green-600 hover:bg-green-700 p-3 rounded-xl"
              >

                <Download size={20} />

              </motion.button>
            )
          }

        </div>

      </div>


      <textarea
        value={giftResult}
        onChange={(e) => setGiftResult(e.target.value)}
        className="w-full h-[850px] bg-slate-950 border border-slate-700 rounded-2xl p-5 font-mono text-sm text-green-300"
      />

    </motion.div>
  )
}